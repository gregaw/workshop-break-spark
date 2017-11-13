# workshop-break-spark
Materials for the 'Let's break Apache Spark' workshop

## Useful commands

```bash
# show master logs
docker exec -it jupyter-spark-master tail -f /opt/spark/logs/spark--org.apache.spark.deploy.master.Master-1-spark-master.out -n 1000

# show slave1 logs
docker exec -it jupyter-spark-slave-1 tail -f /opt/spark/logs/spark--org.apache.spark.deploy.worker.Worker-1-spark-slave-1.out -n 1000

# show slave2 logs
docker exec -it jupyter-spark-slave-2 tail -f /opt/spark/logs/spark--org.apache.spark.deploy.worker.Worker-2-spark-slave-2.out -n 1000

# run bash on jupyter-notebook
docker exec -it jupyter-notebook bash
cd /opt/spark-2.2.0-bin-without-hadoop/

# run spark-submit
bin/spark-submit --executor-memory=1G --conf "spark.driver.memory=1G" --conf "spark.cores.max=10" --conf "spark.executor.cores=1" --master spark://spark-master:7077 examples/src/main/python/pi.py

```
