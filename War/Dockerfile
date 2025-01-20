FROM tensorflow/serving

COPY /SimpleModel /ModelFolder/1

EXPOSE 8501

CMD ["tensorflow_model_server", \
    "--rest_api_port=8501", \
    "--model_name=SimpleReg", \ 
    "--model_base_path=/ModelFolder"]