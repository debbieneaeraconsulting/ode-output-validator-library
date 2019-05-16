import unittest

def assert_results(testcase, results, expected_fail_count):
        fail_count = 0
        for res in results:
            result_partition_printed = False
            for val in res.field_validations:
                if not val.valid:
                    if not result_partition_printed:
                        print("\n========")
                        result_partition_printed = True

                    print("SerialId: %s, Field: %s, Details: %s\n--------\n%s" % (res.serial_id, val.field_path, val.details, res.record))
                    fail_count += 1

        testcase.assertEquals(expected_fail_count, fail_count, "Expected %s failures, got %s failures." % (expected_fail_count, fail_count))
