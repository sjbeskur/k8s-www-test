FROM microsoft/dotnet:2.1.301-sdk
RUN apt-get update -y \
    && apt-get install -y wget curl vim \
    &&  curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh \
    &&  bash nodesource_setup.sh \
    && apt-get install -y nodejs

WORKDIR /src 
COPY www/ ./

RUN npm install && npm run build
RUN dotnet publish --output /output -r linux-x64   
#linux-musl-x64 # use this one for alpine linux

RUN tar -cvzf www.tar.gz -C /output .

ENTRYPOINT [ "/bin/sh","-c","cp www.tar.gz /target"]


