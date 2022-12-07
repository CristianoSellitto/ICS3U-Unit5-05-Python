#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in December 2022
# Formats a mailing address (Canada Post)


def format_mailing_address(
    full_name,
    street_number,
    street_name,
    city,
    province,
    postal_code,
    apartment_number=None,
):
    address = full_name + "\n"
    if apartment_number != None:
        address = address + apartment_number + "-"
    address = (
        address
        + street_number
        + " "
        + street_name
        + "\n"
        + city
        + " "
        + province
        + "  "
        + postal_code
    )

    return address


def main():
    # Gets input and calls the function

    print("\nFormats a mailing address")
    apartment_option = input("\nAre you in an apartment? (y/n): ")
    if apartment_option == "y":
        apartment_number = input("Enter the apartment number: ")
    full_name = input("Enter your full name: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name: ")
    city = input("Enter your city: ")
    province = input("Enter your abbreviated province: ")
    postal_code = input("Enter your postal code: ")
    if apartment_option == "y":
        full_address = format_mailing_address(
            full_name.upper(),
            street_number,
            street_name.upper(),
            city.upper(),
            province.upper(),
            postal_code.upper(),
            apartment_number,
        )
    else:
        full_address = format_mailing_address(
            full_name.upper(),
            street_number,
            street_name.upper(),
            city.upper(),
            province.upper(),
            postal_code.upper(),
        )
    print("\nYour formatted address is:\n\n{}".format(full_address))

    print("\nDone.")


if __name__ == "__main__":
    main()
