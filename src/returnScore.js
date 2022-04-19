import React from 'react';
import PropTypes from 'prop-types';

export default function ReturnScore({ score }) {
    const retscore = String(score);
    return (
      <form method="POST" action="/leaderboard">
        <input name="score" id="score" value={retscore} readOnly />
        <br />
        <br />
        <input type="submit" value="View My Ranking!" id="submit-btn" />
      </form>
    );
}

ReturnScore.propTypes = {
  score: PropTypes.number.isRequired,
};
