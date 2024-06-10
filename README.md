first run the install_translation_package.py

python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. translate.proto
