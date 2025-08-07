test_runs = [
    {
        "id": 101,
        "title": "Login test",
        "status": "passed",
        "tags": {"auth", "smoke"},
        "team": "QA"
    },
    {
        "id": 102,
        "title": "Logout test",
        "status": "failed",
        "tags": {"auth"},
        "team": "QA"
    },
    {
        "id": 103,
        "title": "Profile update",
        "status": "passed",
        "tags": {"ui", "regression"},
        "team": "Dev"
    },
    {
        "id": 104,
        "title": "Token refresh",
        "status": "passed",
        "tags": {"api", "smoke"},
        "team": "QA"
    },
    {
        "id": 105,
        "title": "Search function",
        "status": "failed",
        "tags": {"search", "regression"},
        "team": "QA"
    }
]
count_passed_test = 0
new_dict = {}
unique_tags = set()
failed_tests_list = []

for tests in test_runs:
    if tests["status"].lower() == "passed":
        count_passed_test += 1
    if "smoke" in tests["tags"]:
        print(tests["id"])
    if tests["team"] not in new_dict.keys():
        new_dict[tests["team"]] = []
        new_dict[tests["team"]].append(str(tests["id"]))
    else:
        new_dict[tests["team"]].append(str(tests["id"]))


    for tag in tests["tags"]:
        unique_tags.add(tag)

    if tests["status"].lower() == "failed" and tests["team"].lower() == "qa":
        failed_tests_list.append(tests["title"])

print(f"Успешные тесты: {count_passed_test}")
for key, value in new_dict.items():
    res = " ,".join(value)
    print(f"{key}: {res}")
res_tags = " ,".join(unique_tags)
print(f"Список уникальных тегов: {res_tags}")
final_fails_tests = ", ".join(failed_tests_list)
print(f"Тесты, которые не прошли: {final_fails_tests}")