FROM microsoft/dotnet:2.1.301-sdk
RUN apt-get update -y \
    && apt-get install -y wget curl vim \
    &&  curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh \
    &&  bash nodesource_setup.sh \
    && apt-get install -y nodejs

WORKDIR /src 

COPY www/ ./
RUN dotnet build
RUN npm run build 

ENTRYPOINT [ "dotnet","run" ]


