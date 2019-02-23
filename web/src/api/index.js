import axios from "axios";

const SERVER_BASE_URL = process.env.REACT_APP_SERVER_API;

const serverApi = axios.create({
  baseURL: SERVER_BASE_URL
});

export const predictClassification = async comment => {
  try {
    const response = await serverApi.post("api/predict", [comment]);
    const data = response.data.map(commentResult =>
      Object.keys(commentResult).reduce((acc, cur) => {
        acc[cur] = Boolean(commentResult[cur]);
        return acc;
      }, {})
    );
    console.log(data);
    return data[0];
  } catch (e) {
    console.log(e);
    throw e.data;
  }
};
