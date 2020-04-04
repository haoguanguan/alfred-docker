export PATH=$PATH:/usr/local/bin

NAME="$(whoami)_alfred_bm"
IMAGE='registry.cn-hangzhou.aliyuncs.com/shadow-docker/alfred:bookmarks_v1'
ARG=$@
COMMAND="python /root/src/bookmark.py $ARG"

DOCKER=$(which docker)
EXEC="$DOCKER exec $NAME $COMMAND"

function mainEntry() {
	execOut=$($EXEC 2>&1)
	if [ $? == 0 ]
	then 
		echo $execOut
		return 0
	fi

	if [ "Error: No such container: $NAME" = "$execOut" ]
	then
		###  container not exist, start one
		startContainer
		mainEntry
	fi
}

function startContainer() {
	out=$($DOCKER run --rm -d --name=$NAME -v"$HOME/Library/Application Support/Google/Chrome/Default/Bookmarks":/root/chrome_bookmarks:ro $IMAGE 2>&1)
	if [ $? != 0 ]
	then
		echo "$out"
		exit -1
	fi
}

mainEntry
