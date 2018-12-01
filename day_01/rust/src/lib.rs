#[derive(Clone)]
pub struct AggregateIterator<I> {
    iter: I,
    acc: i32,
}

impl<I> Iterator for AggregateIterator<I>
where
    I: Iterator<Item = i32>,
{
    type Item = i32;

    fn next(&mut self) -> Option<Self::Item> {
        match self.iter.next() {
            Some(a) => {
                self.acc = self.acc + a;
                Some(self.acc)
            }
            None => None,
        }
    }
}

pub trait AggregateTrait {
    fn aggregate(self, acc: i32) -> AggregateIterator<Self>
    where
        Self: Sized + Iterator<Item = i32>,
    {
        AggregateIterator { iter: self, acc }
    }
}

impl<I> AggregateTrait for I
where
    I: Sized + Iterator<Item = i32>,
{
}

#[test]
fn test_aggregate() {
    let a: Vec<i32> = vec![1, 2, 3];
    let expected: Vec<i32> = vec![1, 3, 6];
    let b = a.into_iter().aggregate(0).collect::<Vec<i32>>();
    assert_eq!(b, expected)
}
