from abc import ABC, abstractmethod
from typing import Any, Union, Optional, List, Dict


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:

        self.stream_id = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
        return (data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "type": "Generic",
            "processed": self.processed_count
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.avg_temp: float = 0.0

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:

        list_filter: List[Any] = []

        for data in data_batch:
            if isinstance(data, tuple) and data[0] == criteria:
                list_filter.append(data)
        return (list_filter)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        stats: Dict[str, Union[str, int, float]] = {
            "type": "Sensor",
            "processed": self.processed_count,
            "avg_temp": self.avg_temp
        }
        return (stats)

    def process_batch(self, data_batch: List[Any]) -> str:
        print(
            '\nInitializing Sensor Stream...\n'
            f'Stream ID: {self.stream_id}, Type: Environmental Data'
        )

        result = "[" + ", ".join(f"{k}:{v}" for k, v in data_batch) + "]"
        print(f'Processing sensor batch: {result}')

        list_filter: List[Any] = self.filter_data(data_batch, 'temp')

        temp_tot: float = 0.0
        temp_nb: int = 0

        for n in list_filter:
            try:
                temp_tot += float(n[1])
            except (ValueError, TypeError) as err:
                return (f'[ERROR]: {err}')
            temp_nb += 1

        try:
            self.avg_temp = temp_tot / temp_nb
        except ZeroDivisionError:
            return ('[ERROR]: Temperature data not founded')

        self.processed_count: int = len(data_batch)
        return (
            f'Sensor analysis: {self.processed_count} readings processed, '
            f'avg temp: {self.avg_temp}°C'
        )


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.balance: int = 0

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:

        list_filter: List[Any] = []

        for data in data_batch:
            if isinstance(data, tuple) and data[0] == criteria:
                list_filter.append(data)
        return (list_filter)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        stats: Dict[str, Union[str, int, float]] = {
            "type": "Transaction",
            "processed": self.processed_count,
            "balance": self.balance
        }
        return (stats)

    def process_batch(self, data_batch: List[Any]) -> str:
        print(
            '\nInitializing Transaction Stream...\n'
            f'Stream ID: {self.stream_id}, Type: Financial Data'
        )

        result = "[" + ", ".join(f"{k}:{v}" for k, v in data_batch) + "]"
        print(f'Processing transaction batch: {result}')

        buy_list: List[Any] = self.filter_data(data_batch, 'buy')
        sell_list: List[Any] = self.filter_data(data_batch, 'sell')

        buy_tot: int = 0
        sell_tot: int = 0

        for n in buy_list:
            try:
                buy_tot += int(n[1])
            except (ValueError, TypeError) as err:
                return (f'[ERROR]: {err}')

        for n in sell_list:
            try:
                sell_tot += int(n[1])
            except (ValueError, TypeError) as err:
                return (f'[ERROR]: {err}')

        self.processed_count: int = len(data_batch)
        self.balance = buy_tot - sell_tot
        return (
            f'Transaction analysis: {self.processed_count} operations, '
            f'net flow: {self.balance} units'
        )


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.error_nb: int = 0

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:

        list_filter: List[Any] = []

        for data in data_batch:
            if isinstance(data, str) and data == criteria:
                list_filter.append(data)
        return (list_filter)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        stats: Dict[str, Union[str, int, float]] = {
            "type": "Event",
            "processed": self.processed_count,
            "error": self.error_nb
        }
        return (stats)

    def process_batch(self, data_batch: List[Any]) -> str:
        print(
            '\nInitializing Event Stream...\n'
            f'Stream ID: {self.stream_id}, Type: System Events'
        )

        list_err: List[Any] = self.filter_data(data_batch, 'error')

        self.processed_count: int = len(data_batch)
        self.error_nb = len(list_err)
        return (
            f'Processing event batch: {data_batch}\n'
            f'Event analysis: {self.processed_count} events, '
            f'{self.error_nb} error detected'
        )


class StreamProcessor():
    def polymorphism(
            self, stream: List[Any],
            data_all: List[List[Any]]) -> None:

        for x, y in zip(stream, data_all):
            print(x.process_batch(y))

        print(
            '\n=== Polymorphic Stream Processing ===\n'
            'Processing mixed stream types through unified interface...\n'
        )

        print('Batch 1 Results:')

        for s in stream:
            stat: Dict[str, Union[str, int, float]] = s.get_stats()
            print(
                f"- {stat['type']} data: "
                f"{stat['processed']} processed"
            )

        print('\nStream filtering active: High-priority data only')

        sensor_alert: int = 0
        trans_alert: int = 0

        for s in stream:
            stats = s.get_stats()

            if stats["type"] == "Sensor":
                value = stats.get("avg_temp")
                if isinstance(value, (int, float)) and value > 30:
                    sensor_alert += 1

            if stats["type"] == "Transaction":
                value = stats.get("balance")
                if isinstance(value, (int, float)) and value > 0:
                    trans_alert += 1

        print(
            f'Filtered results: {sensor_alert}  critical sensor alerts, '
            f'{trans_alert} large transaction'
        )


if __name__ == '__main__':
    print('=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===')

    sensor_list: List[Any] = [
        ('temp', 22.5),
        ('humidity', 65),
        ('pressure', 1013)
    ]

    transaction_list: List[Any] = [
        ('buy', 100),
        ('sell', 150),
        ('buy', 75)
    ]

    event_list: List[Any] = ['login', 'error', 'logout']

    stream = StreamProcessor()
    stream_list: List[Any] = [
        SensorStream('SENSOR_001'),
        TransactionStream('TRANS_001'),
        EventStream('EVENT_001')
    ]

    data_all: List[List[Any]] = [
            sensor_list,
            transaction_list,
            event_list
        ]
    stream.polymorphism(stream_list, data_all)

    print('\nAll streams processed successfully. Nexus throughput optimal.')
