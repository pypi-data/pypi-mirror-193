//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var ThreeModel = require('../_base/Three.js').ThreeModel;


class Line3Model extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            start: [0,0,0],
            end: [0,0,0],

        });
    }

    constructThreeObject() {

        var result = new THREE.Line3(
            this.convertVectorModelToThree(this.get('start'), 'start'),
            this.convertVectorModelToThree(this.get('end'), 'end')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);


        this.property_converters['start'] = 'convertVector';
        this.property_converters['end'] = 'convertVector';

        this.property_assigners['start'] = 'assignVector';
        this.property_assigners['end'] = 'assignVector';

    }
}

Line3Model.model_name = 'Line3Model';
Line3Model.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    Line3Model: Line3Model,
};
