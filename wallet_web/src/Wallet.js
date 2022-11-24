
import React from "react";

import * as ReactDOM from "react-dom";

import { Button } from "react-bootstrap";

import "./css/bootstrap.min.css";
import "./css/Wallet.css";

class Wallets extends React.Component {

  constructor(props) {

    super(props);

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

      let element = (

        this.wallets?.map(wallet => (

          <Wallet wallet={wallet} />

        ))

      );

      ReactDOM.render(element, document.getElementById("Wallets"));

    });

  }

  async create_New_Wallet() {

    let response = fetch('createWallet/', {

      method: 'POST',

      body: JSON.stringify({

        wallet_name: this.walletName.value,

      }),

    }
    );

    let result = (await response).json();

    window.location.reload();

  }

  async add_new_address() {

    let response = fetch('createWallet/', {

      method: 'POST',

      body: JSON.stringify({

        wallet: this.walletName.value,

      }),

    }
    );

    let result = (await response).json();


  }

  async create_Transaction(wallet) {

    let response = fetch('startTransaction/', {

      method: 'POST',

      body: JSON.stringify({

        input: wallet,

        output: this.addr.value,

        value: this.value.value,

      }),

    }
    );

    let result = (await response).json();

    window.location.reload();

  }

  componentWillMount() {

    this.get_Wallets();

  }

}

class Wallet extends React.Component {

  render() {

    this.wallet = this.props.wallet;

    return (

      <>
        <div className="Input_DIV">

          <h4>{this.wallet["Wallet"]}:</h4>

          Balance: {this.wallet["Balance"]}, Received: {this.wallet["Received"]}, Sent: {this.wallet["Sent"]}

        </div>

        <div className="Input_DIV">

          <h5>Addresses: </h5>

          {this.wallet["Addresses"].map(addr => (<h6>{addr}</h6>))}

        </div>

        <div className="Input_DIV">

          Address: <input id='Addr' ref={value => this.addr = value} placeholder='Enter Target Address' />,

          Value: <input id='Value' ref={value => this.value = value} placeholder='Enter Value' />

          <Button variant='primary' onClick={this.create_Transaction.bind(this, this.wallet["Wallet"])}>Submit Transaction</Button>

        </div></>
    )

  }

  async create_Transaction(wallet) {

    let response = fetch('startTransaction/', {

      method: 'POST',

      body: JSON.stringify({

        input: wallet,

        output: this.addr.value,

        value: this.value.value,

      }),

    }
    );

    let result = (await response).json();

    window.location.reload();

  }

}

export default Wallets;
