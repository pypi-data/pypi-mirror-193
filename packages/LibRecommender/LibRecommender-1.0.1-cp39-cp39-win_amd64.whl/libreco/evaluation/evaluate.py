"""Utility Functions for Evaluating Data."""
import math
import numbers

import numpy as np
import pandas as pd
from sklearn.metrics import (
    auc,
    balanced_accuracy_score,
    log_loss,
    mean_absolute_error,
    mean_squared_error,
    precision_recall_curve,
    r2_score,
    roc_auc_score,
)

from ..data import TransformedSet
from .computation import (
    build_eval_transformed_data,
    compute_preds,
    compute_probs,
    compute_recommends,
)
from .metrics import (
    ALLOWED_METRICS,
    LISTWISE_METRICS,
    POINTWISE_METRICS,
    map_at_k,
    ndcg_at_k,
    precision_at_k,
    recall_at_k,
)


def _check_metrics(task, metrics, k):
    if not isinstance(metrics, (list, tuple)):
        metrics = [metrics]
    if task == "rating":
        for m in metrics:
            if m not in ALLOWED_METRICS["rating_metrics"]:
                raise ValueError(f"metrics {m} is not suitable for rating task...")
    elif task == "ranking":
        for m in metrics:
            if m not in ALLOWED_METRICS["ranking_metrics"]:
                raise ValueError(f"metrics {m} is not suitable for ranking task...")

    if not isinstance(k, numbers.Integral):
        raise TypeError("k must be integer")

    return metrics


def print_metrics(
    model,
    train_data=None,
    eval_data=None,
    metrics=None,
    eval_batch_size=8192,
    k=10,
    sample_user_num=2048,
    seed=42,
):
    if not metrics:
        metrics = ["loss"]
    metrics = _check_metrics(model.task, metrics, k)

    if model.task == "rating":
        if train_data:
            y_pred, y_true = compute_preds(model, train_data, eval_batch_size)
            print_metrics_rating(metrics, y_true, y_pred, train=True)
        if eval_data:
            y_pred, y_true = compute_preds(model, eval_data, eval_batch_size)
            print_metrics_rating(metrics, y_true, y_pred, train=False)

    elif model.task == "ranking":
        if train_data and POINTWISE_METRICS.intersection(metrics):
            y_prob, y_true = compute_probs(model, train_data, eval_batch_size)
            log_loss_ = log_loss(y_true, y_prob, eps=1e-7)
            print(f"\t train log_loss: {log_loss_:.4f}")
        if eval_data:
            if POINTWISE_METRICS.intersection(metrics):
                y_prob, y_true = compute_probs(model, eval_data, eval_batch_size)
                print_metrics_ranking_pointwise(metrics, y_prob, y_true)
            if LISTWISE_METRICS.intersection(metrics):
                chosen_users = sample_user(eval_data, seed, sample_user_num)
                num_batch_users = max(1, math.floor(eval_batch_size / model.n_items))
                y_true_list = eval_data.user_consumed
                y_reco_list, users = compute_recommends(
                    model, chosen_users, k, num_batch_users
                )
                print_metrics_ranking_listwise(
                    metrics, y_reco_list, y_true_list, users, k
                )


# noinspection PyTypeChecker
def sample_user(data, seed, num):
    np.random.seed(seed)
    unique_users = np.unique(data.user_indices)
    if isinstance(num, numbers.Integral) and 0 < num < len(unique_users):
        users = np.random.choice(unique_users, num, replace=False)
    else:
        users = unique_users
    if isinstance(users, np.ndarray):
        users = list(users)
    return users


def print_metrics_rating(metrics, y_true, y_pred, train=True, **kwargs):
    if kwargs.get("lower_bound") and kwargs.get("upper_bound"):
        lower_bound, upper_bound = (
            kwargs.get("lower_bound"),
            kwargs.get("upper_bound"),
        )
        y_pred = np.clip(y_pred, lower_bound, upper_bound)
    if train:
        for m in metrics:
            if m in ["rmse", "loss"]:
                rmse = np.sqrt(mean_squared_error(y_true, y_pred))
                print(f"\t train rmse: {rmse:.4f}")
    else:
        for m in metrics:
            if m in ["rmse", "loss"]:
                rmse = np.sqrt(mean_squared_error(y_true, y_pred))
                print(f"\t eval rmse: {rmse:.4f}")
            elif m == "mae":
                mae = mean_absolute_error(y_true, y_pred)
                print(f"\t eval mae: {mae:.4f}")
            elif m == "r2":
                r_squared = r2_score(y_true, y_pred)
                print(f"\t eval r2: {r_squared:.4f}")


def print_metrics_ranking_pointwise(metrics, y_prob, y_true):
    for m in metrics:
        if m in ["log_loss", "loss"]:
            log_loss_ = log_loss(y_true, y_prob, eps=1e-7)
            print(f"\t eval log_loss: {log_loss_:.4f}")
        elif m == "balanced_accuracy":
            y_pred = np.round(y_prob)
            accuracy = balanced_accuracy_score(y_true, y_pred)
            print(f"\t eval balanced accuracy: {accuracy:.4f}")
        elif m == "roc_auc":
            roc_auc = roc_auc_score(y_true, y_prob)
            print(f"\t eval roc_auc: {roc_auc:.4f}")
        elif m == "pr_auc":
            precision, recall, _ = precision_recall_curve(y_true, y_prob)
            pr_auc = auc(recall, precision)
            print(f"\t eval pr_auc: {pr_auc:.4f}")


def print_metrics_ranking_listwise(metrics, y_reco_list, y_true_list, users, k):
    for m in metrics:
        if m == "precision":
            precision_all = precision_at_k(y_true_list, y_reco_list, users, k)
            print(f"\t eval precision@{k}: {precision_all:.4f}")
        elif m == "recall":
            recall_all = recall_at_k(y_true_list, y_reco_list, users, k)
            print(f"\t eval recall@{k}: {recall_all:.4f}")
        elif m == "map":
            map_all = map_at_k(y_true_list, y_reco_list, users, k)
            print(f"\t eval map@{k}: {map_all:.4f}")
        elif m == "ndcg":
            ndcg_all = ndcg_at_k(y_true_list, y_reco_list, users, k)
            print(f"\t eval ndcg@{k}: {ndcg_all:.4f}")


def evaluate(
    model,
    data,
    eval_batch_size=8192,
    metrics=None,
    k=10,
    sample_user_num=2048,
    neg_sample=False,
    update_features=False,
    seed=42,
):
    """Evaluate the model on specific data and metrics.

    Parameters
    ----------
    model : Base
        Model for evaluation.
    data : pandas.DataFrame or :class:`~libreco.data.TransformedSet`
        Data to evaluate.
    eval_batch_size : int, default: 8192
        Batch size used in evaluation.
    metrics : list or None, default: None
        List of metrics for evaluating.
    k : int, default: 10
        Parameter of metrics, e.g. recall at k, ndcg at k
    sample_user_num : int, default: 2048
        Number of users for evaluating. Setting it to a positive number will sample
        users randomly from eval data.
    neg_sample : bool, default: False
        Whether to do negative sampling when evaluating.
    update_features : bool, default: False
        Whether to update model's ``data_info`` from features in data.
    seed : int, default: 42
        Random seed.

    Returns
    -------
    results : dict of {str : float}
        Evaluation results for the model and data.

    Examples
    --------
    >>> eval_result = evaluate(model, data, metrics=["roc_auc", "precision", "recall"])
    """
    if isinstance(data, pd.DataFrame):
        data = build_eval_transformed_data(
            model, data, neg_sample, update_features, seed
        )
    assert isinstance(
        data, TransformedSet
    ), "The data from evaluation must be TransformedSet object."
    if not metrics:
        metrics = ["loss"]
    metrics = _check_metrics(model.task, metrics, k)
    eval_result = dict()

    if model.task == "rating":
        y_pred, y_true = compute_preds(model, data, eval_batch_size)
        for m in metrics:
            if m in ["rmse", "loss"]:
                eval_result[m] = np.sqrt(mean_squared_error(y_true, y_pred))
            elif m == "mae":
                eval_result[m] = mean_absolute_error(y_true, y_pred)
            elif m == "r2":
                eval_result[m] = r2_score(y_true, y_pred)

    elif model.task == "ranking":
        if POINTWISE_METRICS.intersection(metrics):
            y_prob, y_true = compute_probs(model, data, eval_batch_size)
            for m in metrics:
                if m in ["log_loss", "loss"]:
                    eval_result[m] = log_loss(y_true, y_prob, eps=1e-7)
                elif m == "balanced_accuracy":
                    y_pred = np.round(y_prob)
                    eval_result[m] = balanced_accuracy_score(y_true, y_pred)
                elif m == "roc_auc":
                    eval_result[m] = roc_auc_score(y_true, y_prob)
                elif m == "pr_auc":
                    precision, recall, _ = precision_recall_curve(y_true, y_prob)
                    eval_result[m] = auc(recall, precision)
        if LISTWISE_METRICS.intersection(metrics):
            chosen_users = sample_user(data, seed, sample_user_num)
            num_batch_users = max(1, math.floor(eval_batch_size / model.n_items))
            y_true_list = data.user_consumed
            y_reco_list, users = compute_recommends(
                model, chosen_users, k, num_batch_users
            )
            for m in metrics:
                if m == "precision":
                    eval_result[m] = precision_at_k(y_true_list, y_reco_list, users, k)
                elif m == "recall":
                    eval_result[m] = recall_at_k(y_true_list, y_reco_list, users, k)
                elif m == "map":
                    eval_result[m] = map_at_k(y_true_list, y_reco_list, users, k)
                elif m == "ndcg":
                    eval_result[m] = ndcg_at_k(y_true_list, y_reco_list, users, k)

    return eval_result
