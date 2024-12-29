## 📖 Question
How to Use TensorFlow Serving on Docker ?

## 💻 Ontech
[![Our Technologies](https://skillicons.dev/icons?i=python,tensorflow,docker)](https://skillicons.dev)

## 💻 Use Model
```shell
docker build -t simpletensor:latest .

docker run -p 8501:8501 simpletensor:latest

curl -d '{"instances":[[5], [10]]}' \
-H "Content-Type: application/json" \
-X POST http://localhost:8501/v1/models/SimpleReg:predict
```