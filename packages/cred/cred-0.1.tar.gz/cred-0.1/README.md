## cred
The module relies on Windows Credentials for storing the passwords.  
It's just a cli tool for managing these credentials.
Generates a 20-character length random string (with upper, lower, punctuation and digits) 
and saves for the given `<target>`.  
Similar to [cmdkey.exe](https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/cmdkey) but actually returns password.

## Usage
`usage: cred {{-r | -w} <target>}`  
  
~~~
> cred -r existing_credential
The password was written on the clipboard.

> cred -r non_existing_credential
Not found.

> cred -w any_string  # existing will be overwritten
Credential written.
~~~

## Installation
~~~
> git clone https://github.com/HenriquedoVal/cred.git
> cd cred
> pip install .
~~~

## Future
Maybe more layers of security would be good, like:
- Cleaning the clipboard after some time
- Request passphrase to get access (would request admin rights)
- Operates as another special user
