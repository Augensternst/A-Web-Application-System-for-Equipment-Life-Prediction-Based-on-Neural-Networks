#!/bin/bash

# 指定要杀死的端口
PORT=8080

# 使用lsof命令找到占用指定端口的进程ID
PID=$(lsof -t -i:$PORT)

# 如果找到了进程ID，则杀死该进程
if [ ! -z "$PID" ]; then
  echo "Killing process on port $PORT with PID $PID"
  kill -9 $PID
else
  echo "No process found on port $PORT"
fi