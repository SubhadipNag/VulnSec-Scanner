import axios from "axios";

const API = axios.create({
    baseURL: "http://api.vulnsec.local:5000"
});

export default API;
