
import React from "react";

import * as ReactDOM from "react-dom";

import { Button } from "react-bootstrap";

import "./css/bootstrap.min.css";
import "./css/Wallet.css";

class Wallets extends React.Component {

  constructor(props) {

    super(props);

    this.get_Wallets();

  }

  render() {

    return (

      <div id="main">

        <div id="NewWallet" className="Input_DIV">

          Wallet Name:

          <input id="WalletName" ref={value => this.walletName = value} placeholder="Enter Wallet Name" />

          <Button variant="primary" onClick={this.create_New_Wallet.bind(this)}>New Wallet</Button>

        </div>

        <div id="Wallets"></div>

      </div>

    );

  }

  async get_Wallets() {

    let response = fetch('getWallets/', {

      method: 'POST',

      body: JSON.stringify({

      }),

    });

    let result = (await response).json();

    result.then((result) => {

      this.wallets = result;

      console.log(this.wallets);

      let element = (



        this.wallets?.map(wallet => (

          <>
            <div className="Input_DIV">

              <h4>{wallet["Wallet"]}:</h4>

              <h5>Balance: {wallet["Balance"]}</h5>

            </div>

            <div className="Input_DIV">

              <h5>Received: {wallet["Received"]}, Sent: {wallet["Sent"]}</h5>

            </div>

            <div className="Input_DIV">

              <h5>Addresses: </h5>

              {wallet["Addresses"].map(addr => (<h6>{addr}</h6>))}

            </div>

            <div className="Input_DIV">

              Address: <input id='Addr' ref={value => this.addr = value} placeholder='Enter Target Address' />,

              Value: <input id='Value' ref={value => this.value = value} placeholder='Enter Value' />

              <Button variant='primary' onClick={this.create_Transaction.bind(this, wallet["Wallet"])}>Submit Transaction</Button>

            </div></>
        ))



      );

      ReactDOM.render(element, document.getElementById("Wallets"));

    });

  }

  async create_New_Wallet() {

    let response = fetch('createWallet/', {

      method: 'POST',

      body: JSON.stringify({

        wallet_name: this.walletName,

      }),

    }
    );

    let result = await response.json();


  }

  async add_new_address() {

    let response = fetch('createWallet/', {

      method: 'POST',

      body: JSON.stringify({

        wallet: this.walletName,

      }),

    }
    );

    let result = await response.json();


  }

  async create_Transaction(wallet) {

    let response = fetch('startTransaction/', {

      method: 'POST',

      body: JSON.stringify({

        input: wallet,

        output: this.addr,

        value: this.value,

      }),

    }
    );

    let result = await response.json();

  }

  componentWillMount() {



    this.get_Wallets();

  }

}

export default Wallets;
