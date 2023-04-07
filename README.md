# multi_form_sample
Djangoの1ページ内に複数のモデルフォームを使用して表示・保存する方法のサンプルコード

## Cloneして動作確認する場合

Cloneして動作確認する場合は、下記の手順でSECRET_KEYを設定してください。

1. Dockerでコンテナを作成起動

```python
python generate_secret_key.py
> SECRET_KEY = 'SECRET_KEYが生成されるのでコピー'
```
2. pythonでgenerate_secret_key.pyを実行して、SECRET_KEYを生成します
SECRET_KEYはコピーしておいてください

app_project/settings.py
```python
SECRET_KEY = 'ここに生成したSECRET_KEYを張り付けてください'
```
3. 生成したSECRET_KEYをsettings.pyのSECRET_KEYに張り付けてください
4. 設定完了