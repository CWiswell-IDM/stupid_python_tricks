# stupid_python_tricks
A bunch of short scripts that illustrate some of how python works

# Kwargs stuff
This is the result of me trying to figure out how this works.
kwargs_example.py

This is meant to simulate creating dictionaries for two anti-mosquito interventions:
A killing-only intervention (Maybe a bugspray, maybe a flyswatter)
A blocking-and-killing intervention (Maybe an insecticide treated bednet, maybe just a blanket)

Either of these interventions would have a start day (the day the intervention first comes into play) and a coverage (percent of people using the intervention).
Additionally, either of these interventions _might_ have an insecticide, but wouldn't need one.A

This allows me to play with calling a simple method like killing_intervention() and pass any of the above parameters, but not implement the coverage and start day stuff for both.

If you run the script at the command line, it simply creates a bunch of these dictionaries and writes them to console.

test_kwargs.py

If you run the tests in test_kwargs.py, it will show test the functionality and show that it does what I think it should.
Additionally, this test file shows some neat testing tricks that you may find helpful:
 - use a setUpClass method to create a bunch of data to test against
 - reusable methods to check the same thing in multiple tests: verify_default_parent_params() and verify_default_blocker_params()
 - use an is_debugging property to write some Debug files to disk if you have trouble. See:
 - - setUp() sets an is_debugging property to False for all tests
 - - test_blocker_sets_local() for an example of turning on is_debbuging here
 - - tearDown() checks to see if is_debbuging is enabled
 - - write_iv_to_disk() generates a file with a name unique to the test method, and writes it to disk


  

