How to start this fxxking complex project:

1. 打开第一个cmd，进入项目中的Vue_Fronted文件夹，运行命令：npm run serve
2. 打开第二个cmd，进入你的redis文件夹，运行redis-cli，然后运行shutdown
3. 进入你的redis文件夹，双击redis-server.exe
4. 打开第三个cmd，进入项目中的DjangoBackend文件夹，运行命令：celery -A DjangoBackend worker -l info -P eventlet -c 10
5. 打开你的pycharm，运行后端