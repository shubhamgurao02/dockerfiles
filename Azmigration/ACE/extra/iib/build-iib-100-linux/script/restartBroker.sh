#!/usr/bin/expect -f

set TARGET_USER [lindex $argv 0]
set TARGET_PASSWORD [lindex $argv 1]
set TARGET_HOST [lindex $argv 2]
set IIB_BROKER [lindex $argv 3]
set IIB_BIN [lindex $argv 4]

spawn ssh $TARGET_USER@$TARGET_HOST ". $IIB_BIN/mqsiprofile && $IIB_BIN/mqsireload $IIB_BROKER"

expect {
authenticity {send "yes\r"; exp_continue}
password: {send "$TARGET_PASSWORD\r"; exp_continue}
eof
}