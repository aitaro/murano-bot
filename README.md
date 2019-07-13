# MURANO BOT をつくろう！

## 開発
茶屋から`env.yaml`をもらってそれ通りに環境変数を設定してください


## デプロイ
デプロイには`env.yaml`が必要
```
$ gcloud functions deploy hello_world --runtime python37 --trigger-http --region asia-northeast1 --env-vars-file='env.yaml'
```
