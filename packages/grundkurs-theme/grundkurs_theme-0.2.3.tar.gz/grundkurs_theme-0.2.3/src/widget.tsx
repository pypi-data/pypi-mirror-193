import { ReactWidget } from '@jupyterlab/apputils';

import React, { useState, useEffect } from 'react';

import { CommandRegistry } from '@lumino/commands';

import { ICellFooter, Cell, ICellModel } from '@jupyterlab/cells';

const StarRating = ({ submit }: { submit: (value: number) => Promise<void> }): JSX.Element => {
  const [rating, setRating] = useState(0);
  const [clicked, setClicked] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    if (submitted) {
      setTimeout(() => {
        setSubmitted(false);
      }, 5000);
    }
  }, [submitted]);

  // @ts-ignore
  const handleClick = (index: number) => {
    setRating(index + 1);
    setClicked(true)
  }

  // @ts-ignore
  const handleSubmit = async () => {
    // logic to handle the submit event goes here
    console.log(`Rating submitted: ${rating}`);
    setClicked(false)
    submit(rating).then(() => setSubmitted(true)).catch(e => console.log(e))
  }

  const ratings = [
    "too easy",
    "easy",
    "good",
    "hard",
    "too hard"
  ]

  return (
    <div className={CELL_FOOTER_DIV_CLASS}>
          <span className="exercise_label">Feedback</span>
      <div className='star-rating'>
        {['😜', '😛', '🙂', '😕' ,'😖'].map((star, index) => (
          <span onClick={() => handleClick(index)} style={{margin: '10px'}}>{star}</span>
        ))}
      </div>
      {clicked && (
        <div style={{display: 'flex', flexDirection: 'column', width: '280px', justifyContent: 'space-around'}}>
        <div className="submitted-message">
          <b>You:</b> <span>The exercise was <b>{ ratings[rating-1] }</b></span> 
          <button className="submit-button" onClick={() => handleSubmit()}>Submit</button>
        </div>
        </div>
      )}
      {submitted && (
          <div className="submitted-message">
            <b>Us:</b> Thank you for submitting your feedback 🙏
          </div>
        )}
    </div>
  );
};

export default StarRating;

/**
 * The CSS classes added to the cell footer.
 */
const CELL_FOOTER_DIV_CLASS = 'gk-cellFeedbackContainer';
//const CELL_FOOTER_BUTTON_CLASS = 'gk-cellFeedbackBtn';

/**
 * Extend default implementation of a cell footer.
 */
export class CellFooterWithButton extends ReactWidget implements ICellFooter {
  /**
   * Construct a new cell footer.
   */
  constructor(commands: CommandRegistry) {
    super();
    this.commands = commands;
  }

  private readonly commands: CommandRegistry;

  render() {
    const metadata = (this.parent as Cell<ICellModel>).model.sharedModel.getMetadata();

    return (
      // TOOD: check for specific tag
      metadata.tags?.includes("exercise") ?
        <StarRating submit={(i) => {
          // We return the Promise, so that the component can react on completion 
          return this.commands.execute('grundkurs:send-feedback', { value: i });
        }} />
        // Return empty tag
        : <></>
    );
  }
}