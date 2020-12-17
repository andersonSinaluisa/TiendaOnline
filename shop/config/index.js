import firebase from 'firebase';
export const APIURL = 'http://localhost:8000';
const firebaseConfig = {
    apiKey: "AIzaSyDCuvXB01abPu2-VzYfqD2PfROse8U3rbw",
    authDomain: "myshop-b462f.firebaseapp.com",
    databaseURL: "https://myshop-b462f.firebaseio.com",
    projectId: "myshop-b462f",
    storageBucket: "myshop-b462f.appspot.com",
    messagingSenderId: "605611048984",
    appId: "1:605611048984:web:49ee708eadbed39c52c36d",
    measurementId: "G-B31JBRN5C1"
  };

export const app = firebase.initializeApp(firebaseConfig)
