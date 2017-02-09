# Add keys to your Bitbucket account over ssh

To use this code fragment, pass it your username and password as a parameter (watch out for *history* if you're using this on the shell!)

Line 8: where most of the magic happens; the key is generated and sent to Bitbucket using curl

Line 10-11: the keys [must have permissions set to 400](https://stackoverflow.com/questions/8193768/trying-to-ssh-into-an-amazon-ec2-instance-permission-error) to be accepted/used for a lot of services.

Line 14: this adds (one of) the bitbucket keys to your known_hosts. They have three of these hosts fyi.
