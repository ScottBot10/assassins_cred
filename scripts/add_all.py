from assassins_cred.io.files import from_csv, write_people

ppl = from_csv("../test_resources/grade 8.csv")

write_people(ppl, "../test_resources/people.csv")
