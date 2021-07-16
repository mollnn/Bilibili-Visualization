source /etc/profile

yarn-daemon.sh stop nodemanager
yarn-daemon.sh stop resourcemanager
hadoop-daemon.sh stop datanode
hadoop-daemon.sh stop namenode

hadoop-daemon.sh start namenode
hadoop-daemon.sh start datanode
yarn-daemon.sh start resourcemanager
yarn-daemon.sh start nodemanager