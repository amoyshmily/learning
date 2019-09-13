
JAR包下载地址：`http://repo1.maven.org/maven2/com/alibaba/fastjson/1.2.47/`

JSONObject responseObj = JSON.parseObject(responseStr);

JSONArray listArray = resObj.getJSONArray("records");

```
int len = listArray.size();
for(int i=0;i<len;i++){
    temp[i]= listArray.getJSONObject(i).getString("DEVICE_ID");
}
```