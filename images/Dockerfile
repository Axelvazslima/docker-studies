FROM node:6-alpine

# The app listens on port 3000, but the container should launch on port 80 (responds to "http://localhost:80")
EXPOSE 3000

# Use apline package manager to install tini
RUN apk add --update tini

# Create directory for app files
# Bash Recap: '-p' stands for "create as many parent dirs as you need"
RUN mkdir -p /usr/src/app

# node uses a "package manager" so it needs to copy in package.json file
WORKDIR /usr/src/app
COPY package.json package.json

# If the first run is successful, run the one after it.
# Different: RUN npm install; npm cache clean. -> ; runs both even if the first command fails.
# Cache clean to keep it clean and small
RUN npm install && npm cache clean

# Copy in all files from current directory
COPY . .

# Starts container with command 'tini -- node ./bin/www'
CMD ["tini", "--", "node", "/bin/www"]