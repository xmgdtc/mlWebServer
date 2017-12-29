# mlWebServer
基于sklearn和Django的一个样例，可以通过http发送数据来进行预测

启动:
manage.py runserver

像这样
```JSON
POST /regre/ HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json
Cache-Control: no-cache


{
	"data":[[1,2,5],[2,3,5],[3,4,5]],
	"tags":[[1],[2],[3]],
	"pdata":[[4,5,6]]
}
```
