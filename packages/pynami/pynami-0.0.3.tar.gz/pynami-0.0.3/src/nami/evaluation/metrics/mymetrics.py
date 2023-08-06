from franky.evaluator import BaseMetric
from seqeval.metrics import f1_score

from nami.registry import METRICS


@METRICS.register_module()
class MyMetrics(BaseMetric):
    def process(self, data_batch, data_samples):
        """Process one batch of data samples.

        The processed results should be stored in ``self.results``, which will
        be used to computed the metrics when all batches have been processed.

        Args:
            data_batch: A batch of data from the dataloader.
            data_samples (Sequence[dict]): A batch of outputs from the model.
        """

        for gt_label, pred_label in zip(data_batch['labels_seq'], data_samples):
            result = dict()
            result['gt_label'] = gt_label
            result['pred_label'] = pred_label
            self.results.append(result)

    def compute_metrics(self, results):
        """Compute the metrics from processed results.

        Args:
            results (dict): The processed results of each batch.

        Returns:
            Dict: The computed metrics. The keys are the names of the metrics,
            and the values are corresponding results.
        """
        # NOTICE: don't access `self.results` from the method.
        metrics = {}
        preds = [r['pred_label'] for r in results]
        targets = [r['gt_label'] for r in results]
        f1 = f1_score(targets, preds)
        metrics['f1'] = f1

        return metrics
