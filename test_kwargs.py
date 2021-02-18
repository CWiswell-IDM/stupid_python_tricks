import json
import unittest
import kwargs_example_bad


class IvKeys:
    Start_Day = 'start_day'
    Coverage = 'coverage'
    Insecticide = 'insecticide'
    Killing_Effectiveness = 'killing_effectiveness'
    Blocking_Effectiveness = 'blocking_effectiveness'




class KwargsTest(unittest.TestCase):
    default_blocking_iv = None
    default_killer_iv = None
    default_iv = None
    default_killer_killing_effectiveness = None
    default_blocker_killing_effectiveness = None
    default_blocker_blocking_effectiveness = None
    default_start_day = None
    default_coverage = None
    all_blocker_keys = [
        IvKeys.Start_Day,
        IvKeys.Coverage,
        IvKeys.Blocking_Effectiveness,
        IvKeys.Killing_Effectiveness
    ]

    # region helper methods
    @classmethod
    def setUpClass(cls) -> None:
        cls.default_blocking_iv = kwargs_example_bad.blocking_killing_iv()
        cls.default_blocker_killing_effectiveness = \
            cls.default_blocking_iv[IvKeys.Killing_Effectiveness]
        cls.default_blocker_blocking_effectiveness = \
            cls.default_blocking_iv[IvKeys.Blocking_Effectiveness]

        cls.default_killer_iv = kwargs_example_bad.killing_intervention()
        cls.default_killer_killing_effectiveness = \
            cls.default_killer_iv[IvKeys.Killing_Effectiveness]

        cls.default_iv = kwargs_example_bad.base_intervention()
        cls.default_start_day = cls.default_iv[IvKeys.Start_Day]
        cls.default_coverage = cls.default_iv[IvKeys.Coverage]

    def setUp(self) -> None:
        self.is_debugging = False
        self.iv_under_test = None
        return

    def write_iv_to_disk(self):
        debug_filename = f'DEBUG_{self.id()}.json'

        with open(debug_filename, 'w') as outfile:
            json.dump(self.iv_under_test, outfile, indent=4, sort_keys=True)
        return

    def verify_default_parent_params(self):
        """
        Verifies that the Start_Day and Coverage parameters
        of an intervention are set to the defaults
        :return:
        """
        self.assertEqual(self.iv_under_test[IvKeys.Coverage],
                         self.default_coverage)
        self.assertEqual(self.iv_under_test[IvKeys.Start_Day],
                         self.default_start_day)

    def verify_default_blocker_params(self):
        """
        Verifies that the killing and blocking effectiveness
        of a blocker intervention are set to the defaults.
        Does NOT verify the Coverage or Start_Day.
        :return:
        """
        self.assertEqual(self.iv_under_test[IvKeys.Blocking_Effectiveness],
                         self.default_blocker_blocking_effectiveness)
        self.assertEqual(self.iv_under_test[IvKeys.Killing_Effectiveness],
                         self.default_blocker_killing_effectiveness)

    def tearDown(self) -> None:
        if self.is_debugging:
            self.write_iv_to_disk()
        return
    # endregion

    # region tests
    def test_default_blocker(self):
        self.iv_under_test = kwargs_example_bad.blocking_killing_iv()
        self.verify_default_parent_params()
        self.verify_default_blocker_params()
        self.assertNotEqual(self.default_killer_killing_effectiveness,
                            self.default_blocker_killing_effectiveness,
                            msg="These tests aren't as useful "
                                "if the two default killing "
                                "effectivenesses are the same. "
                                f"In both cases, got {self.default_killer_killing_effectiveness}.")
        self.assertNotIn(IvKeys.Insecticide,
                         self.iv_under_test.keys())
        return

    def test_default_killer(self):
        self.iv_under_test = kwargs_example_bad.killing_intervention()
        self.assertEqual(self.iv_under_test[IvKeys.Killing_Effectiveness],
                         self.default_killer_killing_effectiveness)
        self.verify_default_parent_params()
        self.assertNotIn(IvKeys.Blocking_Effectiveness,
                         self.iv_under_test.keys(),
                         msg=f"Killing intervention should not have {IvKeys.Blocking_Effectiveness},"
                             f" but had all of these: {self.iv_under_test.keys()}")
        self.assertNotIn(IvKeys.Insecticide,
                         self.iv_under_test.keys())
        return

    def test_blocker_sets_local(self):
        self.is_debugging = True
        specific_blocking_eff = 0.131
        self.iv_under_test = kwargs_example_bad.blocking_killing_iv(
            blocking_eff=specific_blocking_eff
        )
        self.assertEqual(self.iv_under_test[IvKeys.Blocking_Effectiveness],
                         specific_blocking_eff,
                         msg=f"Expected blocking effectiveness of: {specific_blocking_eff}, "
                             f"got {self.iv_under_test[IvKeys.Blocking_Effectiveness]} instead.")
        return

    def test_blocker_sets_parent(self):
        specific_start_day = 13
        self.iv_under_test = kwargs_example_bad.blocking_killing_iv(start_day=specific_start_day)
        self.assertEqual(self.iv_under_test[IvKeys.Start_Day],
                         specific_start_day)
        self.assertEqual(self.iv_under_test[IvKeys.Coverage],
                         self.default_coverage)
        self.verify_default_blocker_params()
        return

    def test_blocker_adds_extra_param(self):
        specific_insecticide = "Hairspray"
        self.iv_under_test = kwargs_example_bad.blocking_killing_iv(
            insecticide=specific_insecticide
        )
        self.assertEqual(self.iv_under_test[IvKeys.Insecticide],
                         specific_insecticide)
        self.verify_default_parent_params()
        self.verify_default_blocker_params()
        return
    # endregion

if __name__ == '__main__':
    unittest.main()
