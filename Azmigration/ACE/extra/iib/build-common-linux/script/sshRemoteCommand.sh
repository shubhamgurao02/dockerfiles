#!/usr/bin/expect -f

set TARGET_USER [lindex $argv 0]
set KEY_FILE [lindex $argv 1]
set TARGET_HOST [lindex $argv 2]
set REMOTE_COMMAND [lindex $argv 3]

set timeout 60

spawn ssh -i $KEY_FILE $TARGET_USER@$TARGET_HOST "$REMOTE_COMMAND"

expect {
authenticity {send "yes\r"; exp_continue}
}