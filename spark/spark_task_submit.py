import argparse
import importlib
import json
from base64 import b64decode

from pyspark.sql import SparkSession


def _decode_arg(value: str) -> str:
    return b64decode(value).decode()


parser = argparse.ArgumentParser()
parser.add_argument("--spark-master-url")
parser.add_argument("--num-executors", type=lambda x: int(_decode_arg(x)))
parser.add_argument("--parameters", type=lambda x: json.loads(_decode_arg(x)))
parser.add_argument("--task-class", type=lambda x: str(_decode_arg(x)))

args = parser.parse_args()

spark = (
    SparkSession.builder.master(args.spark_master_url)
    .config("spark.sql.sources.partitionOverwriteMode", "dynamic")
    .getOrCreate()
)

module_name, class_name = args.task_class.rsplit(".", 1)

module = importlib.import_module(module_name)
Class = getattr(module, class_name)

instance = Class(spark=spark, num_executors=args.num_executors, **args.parameters).run()