#  Copyright 2019 - 2023, Yurii Serhiichuk
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from os import path

from textgenrnn import textgenrnn

script_file_path = path.dirname(__file__) + path.sep


def generate_proverb(
    temperature: float = 0.25, max_gen_length: int = 256, number_of_proverbs: int = 1
) -> list[str]:
    """Generates proverbs.

    :param number_of_proverbs: number of proverbs to generate
    :param temperature: the RNN temperature
    :param max_gen_length: max length of the proverb to be generated
    :return: generated proverbs
    :rtype: list of str
    """
    textgen: textgenrnn = textgenrnn(
        name="ru_proverbs_chars",
        config_path=script_file_path + "ru_proverbs_chars_config.json",
        weights_path=script_file_path + "ru_proverbs_chars_weights.hdf5",
        vocab_path=script_file_path + "ru_proverbs_chars_vocab.json",
    )
    response: list[str] = textgen.generate(
        n=number_of_proverbs,
        temperature=[temperature],
        max_gen_length=max_gen_length,
        progress=False,
        return_as_list=True,
    )
    return response
