# MURANO BOT をつくろう！

## 開発
茶屋から`env.yaml`をもらってそれ通りに環境変数を設定してください


## デプロイ
デプロイには`env.yaml`が必要。また、gcpのmurano-bot projectのアクセス権が必要
```
$ gcloud config set project murano-bot
$ gcloud functions deploy post_tweet --runtime python37 --trigger-http --region asia-northeast1 --env-vars-file='env.yaml'
```
