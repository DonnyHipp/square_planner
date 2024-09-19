import axios from "./axios";

export default class AxiosU {
  static get(path, token) {
    if (token) {
      const config = {
        headers: {
          authentification: token,
        },
      };

      return axios.get(path, config);
    } else {
      return axios.get(path);
    }
  }

  static post(path, field, config) {
    return axios.post(path, field, config);
  }

  static patch(path, field) {
    return axios.patch(path, field);
  }

  static uploadImage(path, fields) {
    const formData = new FormData();
    fields.map((field) =>
      formData.append(field.name, field.file || field.type)
    );

    const config = {
      headers: {
        "content-type": "multipart/form-data",
      },
    };

    return axios.post(path, formData, config);
  }
}
