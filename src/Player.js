export function Player(props) {
    let url = props.url;
    if (props.url == null) {
        url = "defaulturl"
    }
    return (
        <audio hidden id="audio" src={url} autoPlay={true} data-testid="music-player"></audio>
    );
}