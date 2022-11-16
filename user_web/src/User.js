
import React from 'react';

import { Button, Tab, Tabs } from 'react-bootstrap';

import "./css/bootstrap.min.css";
import "./css/User.css";

class User extends React.Component {

  render() {

    return (

      <div style={{ position: "relative" }}>

        <div id="User_Title">

          <h3 style={{ paddingTop: "75px" }}>Welcome to Blockchain Wallet</h3>

        </div>

        <div id="Tabs">

          <Tabs className="justify-content-center">

            <Tab eventKey="login" title="Login" className="User_Tab">

              <User_Login />

            </Tab>

            <Tab eventKey="signup" title="New User" className="User_Tab">

              <New_User />

            </Tab>

          </Tabs>

        </div>

      </div>

    );
  }

}

class User_Login extends React.Component {




  render() {

    return (

      <div className="User_Operation_DIV">

        <div className="Input_DIV">

          <h5>Username:</h5>

          <input id="username" ref={value => this.usernameInput = value} placeholder="Enter Username" />

        </div>

        <div className="Input_DIV">

          <h5>Password:</h5>

          <input id="password" type="password" ref={value => this.passwordInput = value} placeholder="Enter Password" />

        </div>

        <p className="AlertMsg HiddenAlertMsg" id="InputError">Invalid Username or Password!</p>

        <div className="Input_DIV">

          <Button variant="primary" onClick={this.login.bind(this)}>Login</Button>

        </div>

      </div>

    );


  }

  async login() {

    let username = this.usernameInput.value;

    let password = this.passwordInput.value;

    let response = fetch('login/', {

      method: 'POST',

      body: JSON.stringify({

        username: username,

        password: password,

      }),

    }
    );

    let result = (await response).json();

    window.location.href = "/wallet";

  }



}

class New_User extends React.Component {

  render() {

    return (

      <div className="User_Operation_DIV">

        <div className="Input_DIV">

          <h5>Username:</h5>

          <input id="username" ref={value => this.usernameInput = value} placeholder="Enter Username" />

        </div>

        <div className="Input_DIV">

          <h5>Password:</h5>

          <input id="password" type="password" ref={value => this.passwordInput = value} placeholder="Enter Password" />

        </div>

        <div className="Input_DIV">

          <h5>Password:</h5>

          <input id="password" type="password" ref={value => this.passwordInput = value} placeholder="Enter Password" />

        </div>

        <div className="Input_DIV">

          <h5>Confirm Password:</h5>

          <input id="cpassword" type="password" ref={value => this.passwordInput = value} placeholder="Confirm Password" />

        </div>

        <div className="Input_DIV">

          <h5>First Name:</h5>

          <input id="firstname" ref={value => this.firstnameInput = value} placeholder="First Name" />

        </div>

        <div className="Input_DIV">

          <h5>Last Name:</h5>

          <input id="lastname" ref={value => this.lastnameInput = value} placeholder="Last Name" />

        </div>

        <div className="Input_DIV">

          <h5>Email:</h5>

          <input id="email" ref={value => this.emailInput = value} placeholder="Email" />

        </div>

        <div className="Input_DIV">

          <h5>Token:</h5>

          <input id="token" ref={value => this.tokenInput = value} placeholder="Token" />

        </div>

        <div className="Input_DIV">

          <Button variant="primary" onClick={this.register.bind(this)}>Register</Button>

        </div>

      </div>

    );


  }

  async register() {

    let username = this.usernameInput.value;

    let password = this.passwordInput.value;

    let response = fetch('signup/', {

      method: 'POST',

      body: JSON.stringify({

        username: username,

        password: password,

        firstname: this.firstnameInput.value,

        lastname: this.lastnameInput.value,

        email: this.emailInput.value,

        token: this.tokenInput.value,

      }),

    }
    );

    let result = (await response).json();



  }

}

export default User;
