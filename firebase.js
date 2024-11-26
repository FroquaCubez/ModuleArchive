import { initializeApp } from "https://www.gstatic.com/firebasejs/10.0.0/firebase-app.js";
import { getFirestore, doc, getDoc } from "https://www.gstatic.com/firebasejs/10.0.0/firebase-firestore.js";

// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDiJsPOkR96CMUPmoaCagbYCyCkZjvacgg",
  authDomain: "module-archive-5783d.firebaseapp.com",
  projectId: "module-archive-5783d",
  storageBucket: "module-archive-5783d.firebasestorage.app",
  messagingSenderId: "658795417735",
  appId: "1:658795417735:web:ba070aea66dc53b5e3e822",
  measurementId: "G-R9XPPMLBR7"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

