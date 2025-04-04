# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pretend

from warehouse.cache import includeme
from warehouse.cache.interfaces import IQueryResultsCache
from warehouse.cache.services import RedisQueryResults


def test_includeme():
    config = pretend.stub(
        register_service_factory=pretend.call_recorder(lambda *a, **k: None)
    )

    includeme(config)

    assert config.register_service_factory.calls == [
        pretend.call(RedisQueryResults.create_service, IQueryResultsCache)
    ]
