import re
import subprocess
import unittest

class TestGOEnrichContainer(unittest.TestCase):


    def test_consistency(self):

        # Set up variables
        data_path = "./tests/test_data"
        db_path = f"{data_path}/goenrichDB_human.pickle"
        query_path = f"{data_path}/query.tsv"
        expected_output_path = f"{data_path}/expected_output.tsv"
        output_path = f"{data_path}/output.tsv"

        # Run GOEnrich
        subprocess.run(["goenrich",
                        "--goenrichDB", db_path,
                        "-i", query_path,
                        "-o", output_path])

        # Compare output with expected output
        with open(output_path) as output:
            with open(expected_output_path) as expected:
                # Iterate through both files
                for output_string, expected_string in zip(list(output), list(expected)):
                    # Split file lines into lists based on tabs
                    output_list = re.split(r'\t+', output_string.rstrip('\t'))
                    expected_list = re.split(r'\t+', expected_string.rstrip('\t'))

                    # Remove -1.0log(q) calculation result from list, as it is unstable by architecture and q is
                    # already included in insert
                    del output_list[-2]
                    del expected_list[-2]

                    # Assert by line
                    self.assertListEqual(output_list, expected_list)


        # Clean up
        subprocess.run(["rm", output_path])

if __name__ == '__main__':
    unittest.main()