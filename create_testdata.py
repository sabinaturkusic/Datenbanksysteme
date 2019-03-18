from faker import Faker
from faker.providers import address, date_time, company, person, phone_number, profile, BaseProvider

faker = Faker("de_DE")

# create provider
# class Provider(BaseProvider):


# add providers
faker.add_provider(address)
faker.add_provider(date_time)
faker.add_provider(company)
faker.add_provider(person)
faker.add_provider(phone_number)
faker.add_provider(profile)


def generate_person_data():
    SSN = faker.ssn()
    firstName = faker.first_name()
    lastName = faker.last_name()
    address = faker.street_address()
    postCode = faker.postcode()
    location = faker.city()
    return [SSN,
            firstName,
            lastName,
            address,
            postCode,
            location]


def generate_flight_data():
    return;


if __name__ == "__main__":
    person_data = generate_person_data()





