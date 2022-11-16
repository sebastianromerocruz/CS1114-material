hkgtt = ["Yui", "Mio", "Ritsu", "Mugi", "Azuza"]
user_index = input("Enter a band member index ({}-{} only): ".format(0, len(hkgtt) - 1))

print("FETCHING MEMBER NAME...")
try:
    # code that CAN fail
    user_index = int(user_index)
    member = hkgtt[user_index]
except ValueError:
    # what to do IF it DOES fail; index is not an integer
    print("WARNING: Indices must be integers.")
except IndexError:
    # what to do IF it DOES fail; index too large
    print("WARNING: There is no #{} member.".format(user_index))
else:
    # what to do if it DOESN'T fail
    print("The #{} member is {}.".format(user_index, member))
finally:
    # what to do REGARDLESS of whether it does or does not fail
    print("\nPROGRAM FINISHED.")