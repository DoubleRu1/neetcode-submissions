/**
 * Definition of Interval:
 * type Interval struct {
 *    start int
 *    end   int
 * }
 */
func minMeetingRooms(intervals []Interval) int {
    sort.Slice(intervals, func (i,j int)bool{
        return intervals[i].start < intervals[j].start
    })
    visited := make([]bool,len(intervals))
    cnt := 0
    for i := range intervals{
        if !visited[i]{
            cnt ++ 
            visited[i] = true
            cur := []Interval{intervals[i]}
            for j := i; j< len(intervals);j++{
                if !visited[j] && intervals[j].start >= cur[len(cur)-1].end{
                    cur = append(cur,intervals[j])
                    visited[j] = true
                }
            }
            fmt.Println(visited)
            fmt.Println(cur)
        }   
    }
    return cnt
}
