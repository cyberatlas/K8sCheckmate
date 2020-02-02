import valueCheck


test_values_1 = {
	"service": {"port": 80 },
}

test_values_2 = {
	"service": {"port": 81 },
}

test_values_3 = {
	"port": 1,
	"test1": {"port": 2 },
	"test2": {"port": 3 },
	"test3": {"port": 4 },
}

test_values_4 = {
	"port": 5,
	"test1": {"port": 6 },
	"test2": {"port": 7 },
	"test3": {"port": 8 },
}

test_policy_1 = '{ "MAX_PORTS":3, "ALLOWED_PORTS":[80,1,2,3,4]}'

test_policy_2 = '{ "MAX_PORTS":5, "BANNED_PORTS":[81]}'


def test_1_1():
	assert valueCheck.check(test_values_1, test_policy_1) == 0

def test_2_1():
	assert valueCheck.check(test_values_2, test_policy_1) == 1

def test_3_1():
	assert valueCheck.check(test_values_3, test_policy_1) == 1

def test_4_1():
	assert valueCheck.check(test_values_4, test_policy_1) == 5


def test_1_2():
	assert valueCheck.check(test_values_1, test_policy_2) == 0

def test_2_2():
	assert valueCheck.check(test_values_2, test_policy_2) == 1

def test_3_2():
	assert valueCheck.check(test_values_3, test_policy_2) == 0

def test_4_2():
	assert valueCheck.check(test_values_4, test_policy_2) == 0