
Kyaah abstract away SMTP mail operations

Simplify your email message with `kyaah`

      / / \/ /|   /|   /  /
     /_/  / /_|  /_|  /__/
    /  / / /  | /  | /  /

# How to use the library
First we recommend creating a virtual environment `python3 -m venv venv` and then activate it `source venv/bin/activate`

Once that finish now install the library using `pip install kyaah` and wait for the installation basically the library was uploaded using `sdist` (Source Distribution)

After that create a new file let call it `test.py` in the file put the below code

```python
import kyaah
            
sender = "my_email@gmail.com"
receiver = ["receiver_1@gmail.com", "receiver_2@gmail.com"]
passwd = "*********" # use app password
server = "gmail"
subj = f"Hellow world!"
body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt."

kyaah.sendMail(from_usr=sender, to_usr=receiver, svr=server, subject=subj, body=body, mail_passwd=passwd)
```

save the file and navigate to where the file is located in terminal and your are ready to go

`python3 test.py`

## Kyaah with token
There is an OTP code feature if you want to send an OTP code for verification by:

    ____  ___     __
     /   /  / // /_  /| /
    /   /__/ /| /_  / |/

```python
from kyaah import otp

print(otp())
```

You can also specify the length of numbers you want,
by passing an argument of the range number you want in the function like:

```python
from kyaah import otp

print(otp(12))
```

## Kyaah with faker
Use `Faker` for giving you a random email address

      ___        __ __
     /__ /|  // /_ /_/
    /   /-| /| /_ /  |

```python
from kyaah import fk

fk()
```

## Github repository:

- https://github.com/usmanmusa1920/kyaah

Pull requests are welcome
