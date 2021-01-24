from django.db import models
import hashlib


# Account data model (Account)


class Account(models.Model):
    # id (never change)
    id = models.models.AutoField(primary_key=True)

    # Account number (id)
    accountID = models.CharField(max_length=24)

    # Account nickname (name)
    accountName = models.CharField(max_length=24)

    # Account Gender ('1' or '2')
    accountGender = models.CharField(max_length=1)

    # Account Autograph (something write by user)
    accountAutograph = models.CharField(max_length=120)

    # Account register date (time stamp)
    accountRegisterTime = models.models.AutoField()

    # Account Last login time (time stamp)
    accountLastLoginTime = models.models.AutoField()

    # Account password hash (by Secondary sha256 encryption) (Greater than five strings)
    accountPasswordHash = models.models.AutoField()

    # Respond to change accountID request
    def changeName(self, newID: str):
        if not (len(newID) > 24):
            # Everywork is done.
            self.accountID = newID
            super().save()
            return None
        else:
            # Return request.
            return 5

    # Respond to change nickname request
    def changeName(self, newName: str):
        if not (len(newName) > 24):
            # Everywork is done.
            self.accountName = newName
            super().save()
            return None
        else:
            # Return request.
            return 5

    # Respond to change autograph request
    def changeName(self, newAutograph: str):
        if not (len(newAutograph) > 24):
            # Everywork is done.
            self.accountAutograph = newAutograph
            super().save()
            return None
        else:
            # Return request.
            return 5

    # Respond to change Gender request
    def changeGender(self, newGender: int):
        if (newGender == 1) or (newGender == 2):
            # Everywork is done.
            self.accountGender = newGender
            super().save()
            return None
        else:
            # Return request.
            return 5

    # Respond to change password request
    def changePassword(self, newPassword: str):
        if not (len(newPassword) < 5):
            # Everywork is done.
            newPasswordHash = str(
                hashlib.sha256(
                    str(hashlib.sha256(newPassword).digest().encode("utf-8"))
                )
                .digest()
                .encode("utf-8")
            )
            self.accountPasswordHash = newPasswordHash
            super().save()
            return None
        else:
            # Return request.
            return 5
