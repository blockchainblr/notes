echo -e "GET /v1.22/events?since=1455489971 HTTP/1.0\r\n" | nc -U /var/run/docker.sock


20194-fix-typo-api-doc


{"status":"create","id":"7cdd1a3a0911b516e4bf103072e03e1245832b69f692f25f48755b94d5dca777","from":"busybox","Type":"container","Action":"create","Actor":{"ID":"7cdd1a3a0911b516e4bf103072e03e1245832b69f692f25f48755b94d5dca777","Attributes":{"image":"busybox","name":"elegant_bardeen"}},"time":1455505054,"timeNano":1455505054620271712}
{"status":"attach","id":"7cdd1a3a0911b516e4bf103072e03e1245832b69f692f25f48755b94d5dca777","from":"busybox","Type":"container","Action":"attach","Actor":{"ID":"7cdd1a3a0911b516e4bf103072e03e1245832b69f692f25f48755b94d5dca777","Attributes":{"image":"busybox","name":"elegant_bardeen"}},"time":1455505054,"timeNano":1455505054622470949}
{"Type":"network","Action":"connect","Actor":{"ID":"963d7924f5c4531ba1e452ccb59544ba9906e2babbde0a239247c8533e45012e","Attributes":{"container":"7cdd1a3a0911b516e4bf103072e03e1245832b69f692f25f48755b94d5dca777","name":"bridge","type":"bridge"}},"time":1455505054,"timeNano":1455505054637105787}
{"status":"start","id":"7cdd1a3a0911b516e4bf103072e03e1245832b69f692f25f48755b94d5dca777","from":"busybox","Type":"container","Action":"start","Actor":{"ID":"7cdd1a3a0911b516e4bf103072e03e1245832b69f692f25f48755b94d5dca777","Attributes":{"image":"busybox","name":"elegant_bardeen"}},"time":1455505054,"timeNano":1455505054637613225}
{"status":"die","id":"7cdd1a3a0911b516e4bf103072e03e1245832b69f692f25f48755b94d5dca777","from":"busybox","Type":"container","Action":"die","Actor":{"ID":"7cdd1a3a0911b516e4bf103072e03e1245832b69f692f25f48755b94d5dca777","Attributes":{"image":"busybox","name":"elegant_bardeen"}},"time":1455505054,"timeNano":1455505054720209785}
{"Type":"network","Action":"disconnect","Actor":{"ID":"963d7924f5c4531ba1e452ccb59544ba9906e2babbde0a239247c8533e45012e","Attributes":{"container":"7cdd1a3a0911b516e4bf103072e03e1245832b69f692f25f48755b94d5dca777","name":"bridge","type":"bridge"}},"time":1455505054,"timeNano":1455505054785765993}