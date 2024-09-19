import axios from "axios";

const APPLICATION_SERVER = "http://localhost:8000/"

const instance = axios.create({
  baseURL: APPLICATION_SERVER,
  headers: {

  },
});


export default instance;
