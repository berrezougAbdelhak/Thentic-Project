from flask import Flask,redirect,url_for,render_template,request
import requests
import webbrowser

app=Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route("/",methods=["POST","GET"])
def login():
    if request.method=="POST" :
        contract_name=request.form["Cname"]
        contract_symbole=request.form["Csymbl"]
        url = 'https://thentic.tech/api/nfts/contract'
        headers = {'Content-Type': 'application/json'}
        data = {'key': 'W7AwWFBnJMMLeY6NVxZOki3T8cHuTeHV',
        'chain_id': '4',
        'name': contract_name, 
        'short_name': contract_symbole}

        #creates NFT contract on BNB testnet
        r = requests.post(url, json=data, headers=headers)
        print(r.text)
        print(r.json()["transaction_url"])
        webbrowser.open(r.json()["transaction_url"])
        print(contract_name)
        print(contract_symbole)
    return render_template("index.html")

if __name__=="__main__":
    app.run()
